from models.result_models import Result
from models.student_models import Student
from models.parent_models import Parent
from flask import jsonify, request
from api.v1.views import app_views
from sqlalchemy.exc import SQLAlchemyError
from api.v1.views.utils import token_required, require_user_class
from models import storage


@app_views.route("/results", methods=["POST"])
@token_required
@require_user_class("Teacher")
def add_result():
    """
    Add a new result for a student
    ---
    tags:
      - Results
    operations:
      - httpMethod: POST
        summary: Add a new result for a student
        requestBody:
          description: Data to add a new result
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  student_id:
                    type: integer
                    description: ID of the student
                  subject:
                    type: string
                    description: Subject of the result
                  score:
                    type: integer
                    description: Score of the result
        responses:
          '201':
            description: Result added successfully
          '400':
            description: Missing data
          '404':
            description: Student not found
          '500':
            description: Internal server error
    """
    data = request.get_json()
    student_id = data.get("student_id")
    subject = data.get("subject")
    score = data.get("score")

    if not student_id or not subject or not score:
        return jsonify({"error": "Missing data"}), 400

    try:
        student = Student.query.get(student_id)
        if not student:
            return jsonify({"error": "Student not found"}), 404

        new_result = Result(student_id=student_id, subject=subject, score=score)
        new_result.save()
        return jsonify({"message": "Result added successfully"}), 201

    except SQLAlchemyError as e:
        new_result.rollback()
        return jsonify({"error": str(e)}), 500


@app_views.route("/results/<int:student_id>", methods=["GET"])
@token_required
def get_results(student_id):
    """
    Retrieve all results for a student
    ---
    tags:
      - Results
    operations:
      - httpMethod: GET
        summary: Get all results for a student
        parameters:
          - name: student_id
            in: path
            required: true
            description: ID of the student
            schema:
              type: integer
        responses:
          '200':
            description: List of results for the student
            content:
              application/json:
                schema:
                  type: array
                  items:
                    type: object
                    properties:
                      subject:
                        type: string
                        description: Subject of the result
                      score:
                        type: integer
                        description: Score of the result
          '404':
            description: Student not found
          '500':
            description: Internal server error
    """
    try:
        student = Student.query.get(student_id)
        if not student:
            return jsonify({"error": "Student not found"}), 404

        results = Result.query.filter_by(student_id=student_id).all()
        results_list = [
            {"subject": result.subject, "score": result.score} for result in results
        ]

        return jsonify(results_list), 200

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


@app_views.route("/results/<int:result_id>", methods=["PUT"])
@token_required
@require_user_class("Teacher")
def update_result(result_id):
    """
    Update a specific result for a student
    ---
    tags:
      - Results
    operations:
      - httpMethod: PUT
        summary: Update a result for a student
        parameters:
          - name: result_id
            in: path
            required: true
            description: ID of the result
            schema:
              type: integer
        requestBody:
          description: Data to update the result
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  subject:
                    type: string
                    description: Subject of the result
                  score:
                    type: integer
                    description: Score of the result
        responses:
          '200':
            description: Result updated successfully
          '400':
            description: Missing data
          '404':
            description: Result not found
          '500':
            description: Internal server error
    """
    data = request.get_json()
    subject = data.get("subject")
    score = data.get("score")

    if not subject or not score:
        return jsonify({"error": "Missing data"}), 400

    try:
        result = Result.query.get(result_id)
        if not result:
            return jsonify({"error": "Result not found"}), 404

        result.subject = subject
        result.score = score
        storage.save()

        return jsonify({"message": "Result updated successfully"}), 200

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


@token_required
@require_user_class("Teacher")
@app_views.route("/results/<int:result_id>", methods=["DELETE"])
def delete_result(result_id):
    """
    Delete a specific result for a student
    ---
    tags:
      - Results
    operations:
      - httpMethod: DELETE
        summary: Delete a result for a student
        parameters:
          - name: result_id
            in: path
            required: true
            description: ID of the result
            schema:
              type: integer
        responses:
          '200':
            description: Result deleted successfully
          '404':
            description: Result not found
          '500':
            description: Internal server error
    """
    try:
        result = Result.query.get(result_id)
        if not result:
            return jsonify({"error": "Result not found"}), 404

        storage.delete(result)
        storage.save()

        return jsonify({"message": "Result deleted successfully"}), 200

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


from flask import jsonify, request


@app_views.route("/parent/<int:parent_id>/results", methods=["GET"])
@token_required
def get_results_for_parent(parent_id):
    """
    Get all results for all children of a parent
    ---
    tags:
      - Results
    operations:
      - httpMethod: GET
        summary: Retrieve results for all children of a parent
        parameters:
          - name: parent_id
            in: path
            required: true
            description: ID of the parent
            schema:
              type: integer
        responses:
          '200':
            description: List of results for all children of the parent
            content:
              application/json:
                schema:
                  type: array
                  items:
                    type: object
                    properties:
                      student_id:
                        type: integer
                        description: ID of the student
                      student_name:
                        type: string
                        description: Name of the student
                      results:
                        type: array
                        items:
                          type: object
                          properties:
                            subject:
                              type: string
                              description: Subject of the result
                            grade:
                              type: string
                              description: Grade of the result
          '404':
            description: Parent not found
          '500':
            description: Internal server error
    """
    parent = Parent.query.get_or_404(parent_id)
    results = []

    for student in parent.students:
        student_results = {
            "student_id": student.id,
            "student_name": f"{student.firstname} {student.lastname}",
            "results": [],
        }
        for result in student.results:
            student_results["results"].append(
                {"subject": result.subject, "grade": result.grade}
            )
        results.append(student_results)

    return jsonify(results)
