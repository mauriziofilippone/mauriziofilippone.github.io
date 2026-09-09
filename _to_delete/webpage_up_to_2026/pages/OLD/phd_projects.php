<?
$root = "../";
$title = "PhD Projects";
include $root."layout/header.php";
?>

<b>Fully funded PhD scholarship</b>

<p>

Fully-funded PhD scholarship for 3 years in Machine Learning available from September 2015 - EURECOM, Sophia Antipolis, France

<br>
<br>

Applications will be considered from those with degrees in Computer Science, Engineering, Physics, Mathematics, Statistics or related disciplines.

<br>
<br>

The application deadline is **15 August 2015** 

<br>
<br>

Applications should include a CV and the name and contact details of two referees, and should be sent to Dr Maurizio Filippone at Maurizio.Filippone@eurecom.fr

</p>

<br>
<br>

<b>Project description</b>


<p>

Gaussian Processes (GPs) are widely used in applications of data analysis due to their flexibility to model functional relationships between variables.
Such a flexibility stems from the nonparametric nature of GPs that allows one to model a rich class of functions with a minimal set of assumptions.
Another appealing property of GPs is that they are probabilistic, so that any questions about the system under study can be answered using the expressive language of probabilities. 
Examples of application areas where GPs form the core of the statistical analysis, and that will be considered in this project, include pattern recognition, optimization of expensive functions, emulation and calibration of functions implementing simulator of complex systems, and spatio-temporal modeling.

<br>
<br>

Employing GPs becomes problematic for large data sets, because GPs require storing and factorizing an n by n matrix, n being the number of input data; storing this matrix requires O(n^2) space and factorizing it requires O(n^3) operations.
This project aims to investigate techniques to scale computations for GPs without affecting the ability of GPs to quantify uncertainty in parameter estimates and predictions in real problems.
The project will investigate and develop novel inference methods for GPs building on recent work in this area.
In particular, the main topics that will be investigated are sparse GP representations, stochastic gradients for GPs, and GPs with structured inputs. 
It is anticipated that the project will contain an exciting mix of theoretical and applied work.

<br>
<br>

More information can be found here:
<ul>
<li> <a href="http://www.dcs.gla.ac.uk/~maurizio/" target="_blank">www.dcs.gla.ac.uk/~maurizio/</a>
<li> <a href="http://www.dcs.gla.ac.uk/~maurizio/pages/publications.html" target="_blank">www.dcs.gla.ac.uk/~maurizio/pages/publications.html</a>
</ul>


</p>

<br>
<br>


<b>EURECOM</b>

<p>
EURECOM is a graduate school and a research center in communication systems located in Sophia Antipolis, a vibrant science park on the French Riviera. 
Founded by Institut Mines-Télécom, EURECOM’s consortium brings together renowned universities such as Télécom ParisTech, Aalto University (Helsinki), Politecnico di Torino, Technische Universität München (TUM), Norwegian University of Science and Technology (NTNU), Vietnam National University Ho Chi Minh Ville (VNU) and Chalmers University (Sweden) as well as industrial companies such as Swisscom, SFR, Orange, ST Microelectronics, BMW Group Research & Technology, Symantec, Monaco Telecom, SAP, IABG and the Principality of Monaco.
</p>

<br>
<br>




<?
include $root."layout/footer.php";
?>
