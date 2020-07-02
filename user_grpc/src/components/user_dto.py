class UserDTO:

    _ID = "id"
    FIELD_EMAIL = "email"
    FIELD_GENDER = "gender"
    FIELD_FIRST_NAME = "first_name"
    FIELD_LAST_NAME = "last_name"
    FIELD_RECORD_DATE_CREATED = "record_date_created"
    FIELD_RECORD_DATE_LAST_MODIFIED = "record_date_last_modified"

    ACCOUNT_TYPE_MEMBER = 2
    ACCOUNT_TYPE_BUSINESS = 3

    id = None
    email = None
    first_name = None
    last_name = None
    gender = None
    record_date_created = None
    record_date_last_modified = None

    json_array = None

    def __init__(self,
                 id: int = None,
                 email: str = None,
                 first_name: str = None,
                 last_name: str = None,
                 gender: int = None,
                 record_date_created=None,
                 record_date_last_modified=None):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.record_date_created = record_date_created
        self.record_date_last_modified = record_date_last_modified

        self.json_array = {
            self._ID: id,
            self.FIELD_EMAIL: email,
            self.FIELD_FIRST_NAME: first_name,
            self.FIELD_LAST_NAME: last_name,
            self.FIELD_GENDER: gender,
            #self.FIELD_RECORD_DATE_CREATED: record_date_created.strftime("%m/%d/%Y, %H:%M:%S"),
            #self.FIELD_RECORD_DATE_LAST_MODIFIED: record_date_last_modified.strftime("%m/%d/%Y, %H:%M:%S")
        }

    @classmethod
    def make_with_row(cls, row):
        return cls(
            id=row[cls._ID],
            email=row[cls.FIELD_EMAIL],
            first_name=row[cls.FIELD_FIRST_NAME],
            last_name=row[cls.FIELD_LAST_NAME],
            gender=row[cls.FIELD_GENDER],
            record_date_created=row[cls.FIELD_RECORD_DATE_CREATED],
            record_date_last_modified=row[cls.FIELD_RECORD_DATE_LAST_MODIFIED],
        )
