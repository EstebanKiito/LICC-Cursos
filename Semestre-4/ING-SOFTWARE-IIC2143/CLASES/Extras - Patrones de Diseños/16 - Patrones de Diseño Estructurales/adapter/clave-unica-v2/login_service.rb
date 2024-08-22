
class LoginService
    def initialize()
        @users = { "10001-2" => "123",
                  "10002-3" => "333",
                  "12117-4" => "444" }
    end
    def login_user(rut, pass)
        return @users[rut.strip] == pass.strip
    end
end