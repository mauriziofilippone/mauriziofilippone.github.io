<?php
$root = "./";
$title = "Home Page";
include "layout/header.php";
?>

<div id="myphoto">
<img width="160" src="layout/photo.jpeg" alt="Photo" border="0">
</div>

<div>
  <b>Associate Professor</b> with the
<a href="https://cemse.kaust.edu.sa/stat" target="_blank">
  Statistics Program
</a>
at
<a href="https://www.kaust.edu.sa/" target="_blank">
KAUST
</a>
<br>

<p> 
<b>Address</b>:
<br>
4700 King Abdullah University Of Science And Technology
<br> 
Thuwal 23955-6900,
<br>
Kingdom of Saudi Arabia

<p> 

<p> <b>Office</b>: 1-4112

<p> <b>Phone</b>: +966 12 808 7216

<p>
<b>Email Address</b>: maurizio.filippone&nbsp;[at]&nbsp;kaust.edu.sa


<br><br>
<br><br>
<p>
<b>**** Job opportunities available in my group at KAUST ****</b>

<p>
<b>&nbsp;- Postdoc positions in Bayesian Deep Learning</b>:
<a href="http://apply.interfolio.com/142697" target="_blank">
Apply here
</a>

<p>
<b>&nbsp;- Research Technician/Specialist in Bayesian Deep Learning</b>:
<a href="http://apply.interfolio.com/142698" target="_blank">
Apply here
</a>

</div>

<!--
<div id="wordcloud">
<br><br>
<br><br>
<a href="pages/publications.html">
<img width="240"  src="layout/word_cloud_small3.png" alt="Word cloud research" border="0">
</a>
</div>
-->


<div>
<br><br>
<p> <b>NEWS</b> </p>
<?php
$maxnews = 19;
$newsfile = "news.html";
$lines = file($newsfile);
$counter=0;
foreach ($lines as $line_num => $line) {
	if($line != "<br>\n") {
        echo "<p><b>";
        echo substr($line, 0, 8);
        echo "</b>&nbsp;&nbsp;";
        echo substr($line, 9);
        $counter++;
	}
    if($counter >= $maxnews) break;
  }
?>
<br><br>
<a href="news.html">...</a>

</div>

<?php include "layout/footer.php"; ?>
