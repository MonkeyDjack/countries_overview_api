<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="../css/reset.css">
    <link rel="stylesheet" href="../fonts/fonts.css">
    <link rel="stylesheet" href="../css/style.css">
	<title>Map visualisation</title>
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="header-wrapper  clearfix">
                <div class="header_logo">
                    <h1 class="logo--smtxt"><span class="logo--lgtxt">Countries </span>Overview</h1>
                </div>
                <div class="header_navigator">
                    <ul class="header_menu">
                        <li class="header_menu_li"><a href="../index.php" class="menu_li_links">Index</a></li>
                        <li class="header_menu_li"><a href="php/map.php" class="menu_li_links">Json routes</a></li>
                        <li class="header_menu_li"><a href="#" class="menu_li_links">Xml routes</a></li>
                        <li class="header_menu_li"><a href="#" class="menu_li_links">Maps</a></li>
                    </ul>
                </div>
            </div>  
        </div>
    </header>
	 <?php
	 	$population = curl_init();
        $url = 'http://127.0.0.1:1234/population_info';
        
        curl_setopt($population,CURLOPT_URL,$url);
        curl_setopt($population,CURLOPT_HEADER, false);
        curl_setopt($population,CURLOPT_RETURNTRANSFER,true);
        $information = curl_exec($population);
        curl_close($population);
        $informationReceived = (array) json_decode($information);
        ?>

        <h1>Country population</h1>
        <p>click on header to sort(asc/desc)</p>
        <div class="table">
            <div class="table-header">
                <div class="header__item"><a id="country" class="filter__link" href="#">Country</a></div>
                <div class="header__item"><a id="population" class="filter__link filter__link--number" href="#">Population </a></div>
                <div class="header__item"><a id="y_change" class="filter__link filter__link--number" href="#">Yearly change(%)</a></div>
                <div class="header__item"><a id="l_area" class="filter__link filter__link--number" href="#">Land area(Km²)</a></div>
                <div class="header__item"><a id="migrants" class="filter__link filter__link--number" href="#">Migrants</a></div>
                <div class="header__item"><a id="age" class="filter__link filter__link--number" href="#">Medium age</a></div>
                <div class="header__item"><a class="filter__link filter__link--number" href="#">Actions</a></div>
            </div>
                <div class="table-content"> 
               <?php

               if(isset($_POST['delete'])) {
                        if ($_POST['delete'] == 'Delete') {
                            // edit the post with $_POST['id']
                            $country =str_replace(' ', '',$_POST['country_delete']);
                            $url = 'http://127.0.0.1:1234/population_info';
                            $request_url = $url . '/' . $country;

                            $delete = curl_init($request_url);
                            curl_setopt($delete,CURLOPT_RETURNTRANSFER,true);
                            curl_setopt($delete,CURLOPT_URL,$request_url);
                            curl_setopt($delete, CURLOPT_CUSTOMREQUEST, 'DELETE');
                            curl_setopt($delete,CURLOPT_HEADER, false);
                            
                            $response = curl_exec($delete);
                            curl_close($delete);
                            
                            echo $response . PHP_EOL;
                        }
                    }


                if(isset(var))
        foreach ($informationReceived as $informationReceived)  
                {
                    //insert data from json
                    echo '<div class="table-row">';
                    echo '<div class="table-data">'.$informationReceived->country.'</div>';
                    echo '<div class="table-data">'.$informationReceived->population_value.'</div>';
                    echo '<div class="table-data">'.$informationReceived->yearly_change.'</div>';        
                    echo '<div class="table-data">'.$informationReceived->land_area.'</div>'; 
                    echo '<div class="table-data">'.$informationReceived->migrants.'</div>'; 
                    echo '<div class="table-data">'.$informationReceived->med_age.'</div>';
                    
                    echo '<div class="table-data"><form action="" method="POST"><input type="submit" value="Edit">
                   <input type="hidden" name="country_delete" value="'.$informationReceived->country.'"/><input type="submit" name="delete" value="Delete"></form> </div>';
                    echo '</div>';
                }

                    
                    
                
	 ?>
	 </div>
    </div>
<script src="../vendor/jq/jquery-3.2.0.min.js"></script>
<script src="../javascript/map.js"></script>
</body>
</html>