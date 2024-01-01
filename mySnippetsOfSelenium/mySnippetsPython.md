{
	//This document includes my python snippets.

	// Place your snippets for python here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	

	//Python Snippets	
	"Python print": {
	 	"prefix": "print",
		"body": [
			"print($1)",	 		
	 	],
	 	"description": "Python print"
	}
	// Selenium Snippets
	"Selenium implicitly wait": {
	 	"prefix": "implicitly_wait",
		"body": [
			"${1:driver}.implicitly_wait($2)",	
	 	],
	 	"description": "Selenium implicitly wait Ex: driver.implicitly_wait(5) -> wait for 5 sec"
	}

	"Selenium find_element By.XPATH": {
	 	"prefix": "find_element.By.XPATH",
		"body": [
			"${1:driver}.find_element(By.XPATH, '${2:XPATH}')",
	 	],
	 	"description": "Selenium implicitly wait Ex: driver.implicitly_wait(5) -> wait for 5 sec"
	}

	"Selenium find_elements By.XPATH": {
	 	"prefix": "find_elements.By.XPATH",
		"body": [
			"${1:driver}.find_elements(By.XPATH, '${2:XPATH}')",
	 	],
	 	"description": "Selenium implicitly wait Ex: driver.implicitly_wait(5) -> wait for 5 sec"
	}

	"Selenium click()": {
	 	"prefix": "click()",
		"body": [
			".click()",
	 	],
	 	"description": "Selenium implicitly wait Ex: driver.implicitly_wait(5) -> wait for 5 sec"
	}

	

}