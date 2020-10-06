# myinfo
With MyInfo, get your personal info and edit them!

This application is my first Django and Vue app. It is used to experiment with those technologies.

# How to use

## With vagrant (and docker)

This is how I work.

- Clone the directory.
- Open a cmd prompt from the project root directory.
- Type `vagrant up`, wait for the command to complete (may take a couples of minutes). Some vagrant plugins may be installed.
- Check eth0 interfaces to know the VM allocated IP address 
  - If necessary, type `vagrant ssh` to access the VM, then `ifconfig eth0`.
  - If it does not work, try eth1 or another interface.

Application address is `http://VAGRANT_IP_ADDRESS:8000`. Replace `VAGRANT_IP_ADDRESS` with the Vagrant VM IP address.

## With only docker

Warning: no yet tested.

- Clone the directory.
- Open a cmd prompt from the project root directory.
- Type `docker-compose up`.

Application address should be `http://localhost:8000` / `http://127.0.0.1:8000`.

## Without vagrant and docker

Warning: not yet tested.

- Clone the directory.
- Create a virtual Python environment.
- Install required Python packages from requirements.txt, using `pip install -r requirements.txt`.
- Make sure you have a PostgreSQL local server with a database for the myinfo application.
- Modify the DATABASES variable in myinfo/settings.py to use your PostgreSQL local server.
- Open a cmd prompt from the project root directory.
- Type `python manage.py runserver 8000`.

Application address should be `http://localhost:8000` / `http://127.0.0.1:8000`.
