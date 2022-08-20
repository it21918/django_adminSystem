# Clone and run project
```bash
git clone https://github.com/it21918/django_adminSystem.git
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
cd adminSystem
cp adminSystem/.env.example adminSystem/.env
```
edit adminSystem/.env file to define
```vim
SECRET_KEY='test123'
DATABASE_URL=postgres://myprojectuser:password@localhost:/myproject
```
# run development server
```bash
python manage.py runserver
```
