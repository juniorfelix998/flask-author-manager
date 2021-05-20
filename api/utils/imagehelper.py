allowed_extensions = set(['image/jpeg', 'image/png', 'jpeg'])


def allowed_file(filename):
    return filename in allowed_extensions
