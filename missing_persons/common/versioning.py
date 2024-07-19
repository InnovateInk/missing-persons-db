from rest_framework.versioning import URLPathVersioning


class MissingPersonsURLPathVersioning(URLPathVersioning):
    default_version = "v1"
    allowed_versions = ["v1"]
    version_param = "version"
