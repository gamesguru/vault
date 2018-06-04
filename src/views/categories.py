# Categories view

from tabulate import tabulate

from ..models.base import get_session
from ..models.Category import Category
from ..models.Secret import Secret
from ..modules.misc import get_input


def all():
    """
        Return a list of all categories
    """

    return get_session().query(Category).filter(Category.active == 1).order_by(Category.id).all()


def all_table():
    """
        Return a table of categories
    """

    # Retrieve id and name
    cats = [[cat.id, cat.name] for cat in all()]

    if len(cats) > 0:
        return tabulate(cats, headers=['Item', 'Category name'])
    else:
        return 'Empty!'


def pick():
    """
        Ask a user to pick a category
    """

    # Display available categories
    print()
    print(all_table())
    print()

    # Ask user input
    id_ = get_input(message='Select a category: ')

    # Cast as int
    try:
        id_ = int(id_)

        if id_ and exists(id_):
            return id_
    except ValueError:  # Not a valid number!
        pass

    print()
    print('Invalid category number!')

    return False


def exists(id_):
    """
        Check if a category ID exists
    """

    if get_session().query(Category).filter(Category.id == int(id_)).filter(Category.active == 1).first():
        return True

    return False


def get_name(id_):
    """
        Get a category name from a category ID
    """

    if not id_:
        return ''

    cat = get_session().query(Category).filter(
        Category.id == int(id_)).filter(Category.active == 1).first()

    if cat:
        return cat.name

    return ''


def add(name):
    """
        Create a new category
    """

    cat = Category(name=name, active=1)
    get_session().add(cat)
    get_session().commit()

    return True


def add_input():
    """
        Ask user for a category name and create it
    """

    # Ask user input
    name = get_input(message='Category name: ')

    # Return false if name is missing
    if not name:
        return False

    # Create category
    result = add(name=name)

    print()
    print('The category has been created.')

    return result


def rename(id_, new_name):
    """
        Rename a category
    """

    cat = get_session().query(Category).filter(
        Category.id == int(id_)).filter(Category.active == 1).first()

    if cat:
        cat.name = new_name
        get_session().add(cat)
        get_session().commit()

        return True

    return False


def rename_input():
    """
        Rename a category
    """

    # Get id
    id_ = pick()

    # Return false if id is invalid
    if not id_:
        return False

    # Ask user input
    name = get_input(message='Category name: ')

    # Return false if name is missing
    if not name:
        return False

    result = rename(id_, name)

    if result is True:
        print()
        print('The category has been renamed.')

    return result


def delete(id_):
    """
        Disable a category
    """

    cat = get_session().query(Category).filter(
        Category.id == int(id_)).filter(Category.active == 1).first()

    if cat:
        cat.active = 0
        get_session().add(cat)
        get_session().commit()

        return True

    return False


def delete_input():
    """
        Delete a category
    """

    # Get id
    id_ = pick()

    # Return false if id is invalid
    if not id_:
        return False

    # Return false if the category is used
    if is_used(id_):
        print()
        print(
            'The category cannot be deleted because it is currently used by some secrets.')
        return False

    result = delete(id_)

    if result is True:
        print()
        print('The category has been deleted.')

    return result


def is_used(id_):
    """
        Check if a category ID is used by any secret
    """

    if get_session().query(Secret).filter(
            Secret.category_id == int(id_)).first():
        return True

    return False