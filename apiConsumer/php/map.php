<!DOCTYPE html>
<html>
<head>
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
            <table style='width:100%'>
            <tr class="header">
                <th>country</th>
                <th>population_value</th>
                <th>yearly_change </th>
                <th> land_area </th>
                <th> migrants</th>
                <th> med_age </th>
            </tr>
            <tr>
       <?php
        foreach ($informationRecived as $informationRecived)  
                {
                    //insert data from json
                    echo "<tr class='line'>";
                    echo "<td>".$informationRecived->country."</td>";
                    echo "<td>".$informationRecived->population_value."</td>";
                    echo "<td>".$informationRecived->yearly_change."</td>";           
                    echo "<td>".$informationRecived->land_area."</td>"; 
                    echo "<td>".$informationRecived->migrants."</td>"; 
                    echo "<td>".$informationRecived->med_age."</td>";  
                    echo "</tr>";
                }
	 ?>
	 </tr>
         </table>

</body>
</html>