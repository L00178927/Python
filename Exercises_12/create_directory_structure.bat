### This is written by Vinay Reddy B (L00178927)

echo This file is responsible for generating the directory structure of the project.

echo Enter the desired name for the directory you intend to create. 

read directory

if [ -d "directory" ];
then
echo The directory already exists.
else
mkdir $directory
echo New directory called as $directory is created  

cd $directory
mkdir Documentation 
mkdir Examples
mkdir Source
mkdir Tests
echo The directory structure has been successfully established. 
fi