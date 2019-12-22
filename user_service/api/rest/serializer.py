import serpy


class UserSerializer(serpy.Serializer):
    id = serpy.StrField()
    email = serpy.StrField()
    username = serpy.StrField()
    email_verified_at = serpy.Field()
    deactivated_at = serpy.Field()
