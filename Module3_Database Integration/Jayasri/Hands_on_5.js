---------------------------------------------

Task 1: Create the Collection and Insert Documents
------------------------------------------------------
use college_nosql
db.createCollection("feedback")
db.feedback.insertMany([
  { student_id: 1, course_code: "CS101", semester: "2022-ODD", rating: 5, comments: "Excellent", tags: ["good-examples","challenging"], submitted_at: new Date(), attachments: [{filename:"a.pdf",size_kb:100}] },

  { student_id: 2, course_code: "CS101", semester: "2022-ODD", rating: 4, comments: "Nice", tags: ["well-structured"], submitted_at: new Date(), attachments: [{filename:"b.pdf",size_kb:120}] },

  { student_id: 3, course_code: "CS101", semester: "2022-ODD", rating: 2, comments: "Hard", tags: ["challenging"], submitted_at: new Date() },

  { student_id: 4, course_code: "CS102", semester: "2022-ODD", rating: 5, comments: "Great", tags: ["good-examples"], submitted_at: new Date(), attachments: [{filename:"c.pdf",size_kb:90}] },

  { student_id: 5, course_code: "CS102", semester: "2022-ODD", rating: 3, comments: "Okay", tags: ["average"], submitted_at: new Date(), attachments: [{filename:"d.pdf",size_kb:110}] },

  { student_id: 6, course_code: "CS103", semester: "2022-ODD", rating: 1, comments: "Poor", tags: ["challenging"], submitted_at: new Date(), attachments: [{filename:"e.pdf",size_kb:80}] },

  { student_id: 7, course_code: "CS103", semester: "2021-EVEN", rating: 4, comments: "Good", tags: ["well-structured"], submitted_at: new Date(), attachments: [{filename:"f.pdf",size_kb:150}] },

  { student_id: 8, course_code: "CS104", semester: "2022-ODD", rating: 5, comments: "Best", tags: ["good-examples","well-structured"], submitted_at: new Date(), attachments: [{filename:"g.pdf",size_kb:200}] },

  { student_id: 9, course_code: "CS104", semester: "2021-EVEN", rating: 2, comments: "Bad", tags: ["challenging"], submitted_at: new Date(), attachments: [{filename:"h.pdf",size_kb:130}] },

  { student_id: 10, course_code: "CS101", semester: "2022-ODD", rating: 4, comments: "Nice", tags: ["good-examples"], submitted_at: new Date() }
])
db.feedback.countDocuments() 
------------------------------------------

TASK 2 QUERIES (WITH NUMBERS)
-------------------------------------------
65
db.feedback.find({ rating: 5 })
66
db.feedback.find({ course_code: "CS101", tags: "challenging" })
67
db.feedback.find({}, { student_id: 1, course_code: 1, rating: 1, _id: 0 })
68
db.feedback.updateMany(
  { rating: { $lt: 3 } },
  { $set: { needs_review: true } }
)
69
db.feedback.updateMany(
  { needs_review: true },
  { $push: { tags: "reviewed" } }
)
70
db.feedback.deleteMany({ semester: "2021-EVEN" })
-----------------------------------------------
  Task 3: Aggregation Pipeline
-------------------------------------------------
  71
db.feedback.aggregate([
  { $match: { semester: "2022-ODD" } },
  {
    $group: {
      _id: "$course_code",
      avg_rating: { $avg: "$rating" },
      total_feedback: { $sum: 1 }
    }
  },
  { $sort: { avg_rating: -1 } }
])
72
db.feedback.aggregate([
  { $match: { semester: "2022-ODD" } },
  {
    $group: {
      _id: "$course_code",
      avg_rating: { $avg: "$rating" },
      total_feedback: { $sum: 1 }
    }
  },
  {
    $project: {
      average_rating: { $round: ["$avg_rating", 1] },
      total_feedback: 1
    }
  },
  { $sort: { average_rating: -1 } }
])
73
db.feedback.aggregate([
  { $unwind: "$tags" },
  {
    $group: {
      _id: "$tags",
      count: { $sum: 1 }
    }
  },
  { $sort: { count: -1 } }
])
74
db.feedback.createIndex({ course_code: 1 })
75 
db.feedback.find({ course_code: "CS101" }).explain("executionStats")
