from flask import Blueprint, jsonify, request
from app import db
from courses.models import Course, Student, Enrollment

courses_bp = Blueprint("courses", __name__, url_prefix="/api/courses")


def make_response_json(data, status_code=200):
    return jsonify({
        "status": "success",
        "data": data
    }), status_code


# GET ALL COURSES
@courses_bp.route("/", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return make_response_json([course.to_dict() for course in courses])


# CREATE COURSE
@courses_bp.route("/", methods=["POST"])
def create_course():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data"}), 400

    required = ["name", "code", "credits"]

    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"],
        department_id=data.get("department_id")
    )

    db.session.add(course)
    db.session.commit()

    return make_response_json(course.to_dict(), 201)


# GET SINGLE COURSE
@courses_bp.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return make_response_json(course.to_dict())


# UPDATE COURSE
@courses_bp.route("/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)

    data = request.get_json()

    course.name = data.get("name", course.name)
    course.code = data.get("code", course.code)
    course.credits = data.get("credits", course.credits)

    db.session.commit()

    return make_response_json(course.to_dict())


# DELETE COURSE
@courses_bp.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)

    db.session.delete(course)
    db.session.commit()

    return jsonify({"message": "Course deleted successfully"}), 200


# GET STUDENTS OF A COURSE
@courses_bp.route("/<int:course_id>/students", methods=["GET"])
def get_students(course_id):

    students = (
        db.session.query(Student)
        .join(Enrollment)
        .filter(Enrollment.course_id == course_id)
        .all()
    )

    return make_response_json([student.to_dict() for student in students])