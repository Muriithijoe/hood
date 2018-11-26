# Neighborhood-Update

#### This is a site for getting updates about neighborhood, {26/11/2018}

#### By **Joe Muriithi**

## Description

This is site where members of a certain neighborhood can join and post about new developments in
the neighborhood.Information about nearby businesses, police and hospitals is also on the site.

## Behaviour Driven Development
The program should return all projects on the directories page

Given:All projects

When: Url is changed to directory page

Then: All projects are displayed

Program should show the project with the highest number of votes on the caraousel on the home page

Given:A Project with the highest votes

When: Home page is accessed

Then: Project with highest votes is displayed.

Admin site should be displayed when "admin/" url is chosen

Given: An admin url

When: User enters admin url in browser

Then: Admin Login is displayed

User authentication occurs when Admin tries to Login

Given:Admin page is accessed

When: User tries to login

Then: User details are authenticated to confirm if user is an admin

User session should end when logout url is chosen

Given:Logout option is given

When: User chooses logout option

Then: User session is ended



## Setup/Installation Requirements
* git clone this repo https://github.com/Muriithijoe/hood.git
* open terminal and open the project
* make sure you have atom to see code
* runserver

## Known Bugs

~There are no known bugs.

## Technologies Used

~Python3.7

~HTML5

~Materialize

~CSS

~bootstrap3

~Atom as editor

~Heroku as hosting site

## Support and contact details

email me at joeace2000@gmail.com

### License

MIT License

Copyright (c) [2018] [Joe Muriithi Wambugu]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
