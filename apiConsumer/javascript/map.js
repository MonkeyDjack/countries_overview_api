fetch('http://127.0.0.1:1234/population_info')
	.then(response => {
		return response.json();
	})
	.then(population => {
		console.log(population)
	})