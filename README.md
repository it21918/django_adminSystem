# Clone and run project
```bash
git clone https://github.com/it21998/devopsAdmin.git
python -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
cd adminSystem
cp adminSystem/.env.example student_management/.env
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
