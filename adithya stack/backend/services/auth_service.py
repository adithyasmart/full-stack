from models.user import User

class AuthService:
    @staticmethod
    async def authenticate(username, password):
        user = await User.query.filter_by(username=username).first()
        if user and user.authenticate(password):
            # Generate token logic here
            return {"token": "generated_token"}
        return None

    @staticmethod
    async def get_user_from_token(token):
        # Decode token and fetch user
        pass
