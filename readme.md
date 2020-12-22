# What?

RayStarter is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template to quickly output a customized starter
project to use C and Raylib, compiled in gcc with python (not Scons or similar system), letting you very easily set up the project
without being familiar with the many C Make alternatives and their syntaxes.

Note since this template focuses on very small jam games you will benefit from having `upx` on your path, 
downloaded [here,](https://upx.github.io) as this will be used to minimize your binary size after the fact.

# Why?

I wanted a basic C/Raylib project structure that was the least pain and the least configuration, with the intention of making small games.

Eventually I will be adding convenience single header libs for my personal use aswell.

# Usage

- Make sure you have Python 3+
- Install [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- Install raylib by placing the raylib headers in /usr/include/raylib or equivalent windows folder(see your gcc folder and look for an include folder) and
the `libraylib.a` static bindings into /usr/lib or equivalent windows folder(see your gcc folder and look for a lib folder.)
- Run `cookiecutter https://github.com/JonSnowbd/RayStarter` in your terminal in the folder that contains your projects. The questionnaire
will run you through it all and output your ready to go raylib project.
- Enjoy. Thats all you need to do 