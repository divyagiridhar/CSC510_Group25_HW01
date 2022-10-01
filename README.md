
<img src="https://github.com/divyagiridhar/CSC510_Group25_HW02/blob/main/data/images/LUA%20to%20Python%20Banner.png">

<div align="center">
 
  <a href="https://github.com/divyagiridhar/CSC510_Group25_HW02">
    <img src="https://img.shields.io/github/repo-size/divyagiridhar/CSC510_Group25_HW02?color=brightgreen">
  </a>
  <a href="https://github.com/divyagiridhar/CSC510_Group25_HW02/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/divyagiridhar/CSC510_Group25_HW02">
  </a>
  <a href="https://github.com/divyagiridhar/CSC510_Group25_HW02/graphs/commit-activity">
    <img src="https://img.shields.io/github/commit-activity/w/divyagiridhar/CSC510_Group25_HW02?color=blueviolet">
  </a>
  <a href="https://github.com/divyagiridhar/CSC510_Group25_HW02/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/divyagiridhar/CSC510_Group25_HW02?color=important">
  </a>
  <a href="https://zenodo.org/badge/latestdoi/532400224">
    <img src="https://zenodo.org/badge/532400224.svg" alt="DOI"></a>
  </a>
  <a href="https://github.com/divyagiridhar/CSC510_Group25_HW02/actions/workflows/python-app.yml">
    <img src="https://github.com/divyagiridhar/CSC510_Group25_HW02/actions/workflows/python-app.yml/badge.svg">
  </a>
  <a href="https://codecov.io/gh/dhruvpatel-9/CSC510_Group25_HW02" > 
 <img src="https://codecov.io/gh/dhruvpatel-9/CSC510_Group25_HW02/branch/main/graph/badge.svg?token=EQLJ15FY7H"/> 
 </a>
<a href="https://github.com/divyagiridhar/CSC510_Group25_HW02/actions/workflows/Coverage.yml">
    <img src="https://github.com/divyagiridhar/CSC510_Group25_HW02/actions/workflows/Coverage.yml/badge.svg">
  </a>

</div>

<h2> Table of Contents </h2>
<li> 
<a href="#overview"> Overview </a> 
</li>
<li> 
<a href="#target audience"> Target Audience </a> 
</li>
<li> 
<a href="#classes"> Classes and Test Case</a>
</li>
<li> 
<a href="#gs"> Getting Started </a>
</li>
<li> 
<a href="#ins"> Instructions to run the Tests and Display Results </a>
</li>
<li> 
<a href="#licenses"> License </a> 
</li>
<li> 
<a href="#cb"> Contributors </a>
</li>
<li> 
<a href="#help"> Help </a>
</li>

<h2 id = "overview"> Overview </h2>

> Converting LUA Code to Python 

Lua is a powerful scripting language with several functionalities such as : 
  <ol>
    <li> Procedural programming </li>
    <li> Object-oriented programming </li>
    <li> Functional programming </li>
    <li> Data-driven programming </li>
  </ol>

This repo seeks to translate a Lua code into Python while maintaining its essential logic and functionalities.

<br>

<h2 id = "target audience"> Target Audience </h2>

This repo is for users who want to get detailed understanding of LUA working system and converting it into Python

The source LUA code can be found <a href = "https://github.com/txt/se22/blob/main/etc/pdf/csv.pdf"> here </a>

<br>


<h2 id = "classes"> Classes and Test Case </h2>

The Python Code for `Cols`, `Data`, `Num`, `Row`, `Sym` and `Utils` is available in this <a href="https://github.com/divyagiridhar/CSC510_Group25_HW02/tree/main/code"> repo </a>
<br><br>
The Test Cases for all the Classes are also available <a href = "https://github.com/divyagiridhar/CSC510_Group25_HW02/blob/main/tests/test_lua.py"> here </a>
<br><br>


<table>
  <tr>
    <td align="center" colspan = "6"> Classes </td>
  </tr>
  
  <tr>
    <td> <a href = "https://github.com/divyagiridhar/CSC510_Group25_HW02/blob/main/code/Cols.py"> Cols </a> </td>
    <td> <a href = "https://github.com/divyagiridhar/CSC510_Group25_HW02/blob/main/code/Data.py"> Data </a> </td>
    <td> <a href = "https://github.com/divyagiridhar/CSC510_Group25_HW02/blob/main/code/Num.py">Num </a> </td>
    <td> <a href = "https://github.com/divyagiridhar/CSC510_Group25_HW02/blob/main/code/Row.py"> Row </a> </td>
    <td> <a href = "https://github.com/divyagiridhar/CSC510_Group25_HW02/blob/main/code/Sym.py"> Sym </a> </td>
    <td> <a href = "https://github.com/divyagiridhar/CSC510_Group25_HW02/blob/main/code/Utils.py"> Utils </a> </td>
  </tr>

  
</table>

<br>


<h2 id = "gs"> Getting Started </h2>

> To run these programs make sure you have python version 3 and pytest version 7 installed.

``` bash
python --version
```

> Run the following command to install all requirements. 

``` bash
pip install -r requirements. txt
``` 

<h2 id = "ins"> Instructions to run the Tests and Display Results </h2>

> Initially you need to add the following paths to the Environment variables under `System Requirements\Advanced\Environment Variables\System Variables\Path\New`
``` bash
...<path to directory>\CSC510_Group25_HW02-main\code
...<path to directory>\CSC510_Group25_HW02-main\data
``` 

`For Example` <br>
<img src="data/images/Screenshot 2022-09-27 114745.png" width='300'>

> Open the following directory in Command Prompt using
``` bash
cd ...<path to directory>\CSC510_Group25_HW02-main
```

> To check whether the test caes are running correctly, execute the following command.
``` bash
pytest tests/test_lua.py -v
``` 
`Example output` <br>
<img src="data/images/Screenshot 2022-09-27 114557.png">

> To view the results of tasks, execute the following command.
``` bash
python code/main.py
``` 
`Example output` <br>
<img src="data/images/Screenshot 2022-09-27 120034.png">
<img src="data/images/Screenshot 2022-09-27 120106.png">

<br>

<h2 id = "licenses"> Licenses </h2>

> <a href="https://github.com/divyagiridhar/CSC-510-Group-25/blob/main/LICENSE"> MIT </a> License is used in this project. 
<br>

<h2 id = "help"> Help </h2>
You can email any queries to the contributors - 
<br>
<li>
    <a href = "mailto: divyagiridhar97@gmail.com">Divya Giridhar</a>
</li>
<li>
    <a href = "mailto: shreyastitus@gmail.com">Shreyas Titus</a>
</li>
<li>
    <a href = "mailto: dpatel49@ncsu.edu">Dhruv Patel</a>
</li>
<li>
    <a href = "mailto: rghevar@ncsu.edu">Ravi Ghevariya</a>
</li>
<li>
    <a href = "mailto: mrpatel8@ncsu.edu">Manan Patel</a>
</li>
<br>

<hr>
  <p id="cb" align = "center">
  | &nbsp;Dhruv Patel &nbsp;|&nbsp; Manan Patel &nbsp;|&nbsp; Ravi Ghevariya &nbsp;|&nbsp; Divya Giridhar &nbsp;|&nbsp; Shreyas Titus |
  </p>
  
<hr>
