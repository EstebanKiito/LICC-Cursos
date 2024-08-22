require_relative 'score_improver.rb'

students = []
students.push(Student.new(3))
students.push(Student.new(4))
students.push(Student.new(5))
students.push(Student.new(6.2))
students.push(Student.new(5.5))

ScoreImprover.new.improve(students)

students.each do |student|
    puts student.score
end