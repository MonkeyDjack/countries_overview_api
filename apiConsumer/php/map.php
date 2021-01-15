<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="../css/reset.css">
    <link rel="stylesheet" href="../fonts/fonts.css">
    <link rel="stylesheet" href="../css/style.css">
	<title>Map visualisation</title>
</head>
<body>
	 <?php
	 	$population = curl_init();
        $url = 'http://127.0.0.1:1234/population_info';
        
        curl_setopt($population,CURLOPT_URL,$url);
        curl_setopt($population,CURLOPT_HEADER, false);
        curl_setopt($population,CURLOPT_RETURNTRANSFER,true);
        $information = curl_exec($population);
        curl_close($population);
        $informationRecived = (array) json_decode($information);
        ?>

        <h1>Country population</h1>
        <p>click on header to sort(asc/desc)</p>
        <div class="table">
            <div class="table-header">
                <div class="header__item"><a id="country" class="filter__link" href="#">Country</a></div>
                <div class="header__item"><a id="population" class="filter__link filter__link--number" href="#">Population </a></div>
                <div class="header__item"><a id="y_change" class="filter__link filter__link--number" href="#">Yearly change</a></div>
                <div class="header__item"><a id="l_area" class="filter__link filter__link--number" href="#">Land area</a></div>
                <div class="header__item"><a id="migrants" class="filter__link filter__link--number" href="#">Migrants</a></div>
                <div class="header__item"><a id="age" class="filter__link filter__link--number" href="#">Medium age</a></div>
            </div>
                <div class="table-content"> 
               <?php
        foreach ($informationRecived as $informationRecived)  
                {
                    //insert data from json
                    echo '<div class="table-row">';
                    echo '<div class="table-data">'.$informationRecived->country.'</div>';
                    echo '<div class="table-data">'.$informationRecived->population_value.'</div>';
                    echo '<div class="table-data">'.$informationRecived->yearly_change.'%</div>';        
                    echo '<div class="table-data">'.$informationRecived->land_area.'Km²</div>'; 
                    echo '<div class="table-data">'.$informationRecived->migrants.'</div>'; 
                    echo '<div class="table-data">'.$informationRecived->med_age.'</div>';  
                    echo '</div>';
                }
	 ?>
	 </div>
    </div>
<script src="../vendor/jq/jquery-3.2.0.min.js"></script>
<script src="../javascript/map.js"></script>
</body>
</html>