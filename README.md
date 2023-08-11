
# AirBnB clone

This project is a copy of the AirBnB website.


## Steps

### 1. The console
- Create a data model

- manage (create, update, destroy, etc) objects via a console / command interpreter

- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

! [alt text] (https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230811%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230811T155758Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=85a83bb5b633de6e1c7b0210dc4328b28b6e6dd794ad64970ee3b0b9b94cf16c)
#### Run The console Locally

Clone the project

```bash
  git clone https://github.com/aplusJsDev/AirBnB_clone.git
```

Go to the project directory

```bash
  cd AirBnB_clone
```

Then Run:

```bash
  ./console.py
```
