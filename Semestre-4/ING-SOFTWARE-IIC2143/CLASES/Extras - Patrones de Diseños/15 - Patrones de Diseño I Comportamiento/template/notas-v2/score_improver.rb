class Student
    attr_accessor :score
    def initialize(s)
        @score = s
    end
end


class ScoreImprover
    # este metodo es un template-metodo
    # porque tiene un pedaso faltante
    # el metodo measure-difference es abstract (no existe en esta clase)
    def improve(students)
        # paso 1: medir la diferencia
        diff = measureDifference(students)
        # paso 2: sumar a todos la diferencia
        sumAll(diff)
        # el metodo plantilla encapsula un algoritmo, donde uno o mas de sus pasos llama a un método abstracto
    end
    def sumAll(diff)
        students.each do |student|
            student.score = student.score + diff
        end
    end
    def measureDifference(students)
        raise NotImplementedError
    end
end


class Improve7 < ScoreImprover
    # las clases hijas definen el paso faltante de la plantilla
    def measureDifference(students)
        maxScore = 1
        students.each do |student|
            if  maxScore < student.score
                maxScore = student.score
            end
        end
        diff = 7 - maxScore
        return diff
    end
end

# el metodo plantilla nos permite re-utilizar los varios pasos
# ya que solo tenemos que agregra la plantilla el paso faltante
# el paso faltante varia dependiendo de la clase hija
class Improve4 < ScoreImprover
    def measureDifference(students)
        minScore = 7
        students.each do |student|
            if  minScore > student.score
                minScore = student.score
            end
        end
        diff = 4 - minScore
        return diff
    end
end