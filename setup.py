from setuptools import setup, find_packages

setup(
    name="Practica_ibd_AlexisMachado",
    version="0.0.1",
    author="Jhon Alexis Machado Rodriguez",
    author_email="jmachadoa12@gmail.com",
    description="Práctica EA1 Proyecto integrador: Ingesta de datos desde un API a SQLite y Muestra en Excel. 🚀",
    py_modules=["Práctica EA1_Ingestión_Datos_API"],
    install_requires=[
        'requests',
        "pandas",
        "openpyxl"
    ]
)