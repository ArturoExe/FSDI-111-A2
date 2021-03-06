from app.database import get_db


def output_formatter(results):  #results is a tuple of tuples
    out=[]                      #empty list

    for r in results:           #for each loop
        r_dictionary={
            "id":r[0],
            "first_name":r[1],
            "last_name":r[2],
            "hobbies":r[3],
            "active":r[4]
        }
        out.append(r_dictionary)
    return out


def insert(user_dict):

    value_tuple=(
        user_dict.get("first_name"),
        user_dict.get("last_name"),
        user_dict.get("hobbies")
    )

    statement="""
    INSERT INTO user (
        first_name,
        last_name,
        hobbies
    ) VALUES (?,?,?) 
    """
    # ? is a placeholder for the variables
    cursor=get_db()
    cursor.execute(statement,value_tuple)
    cursor.commit()
    cursor.close()

def scan():
    cursor=get_db().execute("SELECT * FROM user WHERE active=1",())
    results=cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk):
    cursor=get_db().execute("SELECT * FROM user WHERE id=?",(pk,))#(pk,) is a tuple with a single value
    results=cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def update(pk, user_data):
    value_tuple = (
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
        pk
    )
    statement = """
        UPDATE user SET first_name=?, last_name=?, hobbies=? WHERE id=?
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()