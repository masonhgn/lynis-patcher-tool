import subprocess







"""
	***********************************************************************************

	Function Name: runCommand

	Description: Attempts to run whatever argument is passed in as a linux command.
	
	Params:
		- cmd: the command you want to run

	Returns:
		- True if the command is successfully run
		- False if the command fails

	***********************************************************************************
"""
def runCommand(cmd):
	try:
		msg = subprocess.run(cmd, shell=True,check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print(msg.stdout.decode())
		return True
	except subprocess.CalledProcessError as e:
		print(e.stderr.decode())
		return False








"""
	***********************************************************************************

	Function Name: parseFile

	Description: Attempts to open a file with the name of the passed in argument, and parse it into a list of strings.
	
	Params:
		- fileName: the name of the file you want to open and parse

	Returns:
		- result, the newly created list

	***********************************************************************************
"""
def parseFile(fileName):
	result = ''
	with open(fileName, 'r') as file:
		for line in file:
			for word in line.split():
				result += word + ' '
	return result









"""
	***********************************************************************************

	Function Name: patchSuggestions

	Description: Takes in a list of suggestions generated by the Lynis report, and searches for them in the 
	suggestions dictionary. If it is found, the corresponding command is run to patch that vulnerability.
	
	Params:
		- report: A list of strings that is just the Lynis report file parsed into a list of lines

	Returns:
		- void

	***********************************************************************************
"""
def patchSuggestions(report):
	for line in report:
		if line in suggestionsDict:
			success = runCommand(suggestionsDict[line])
			if success:
				print("Command \'", suggestionsDict[line], "\' succeeded")
			else:
				print("Command \'", suggestionsDict[line], "\' failed")



def main():
    print("Welcome to the Lynis Security Vulnerability Patcher.")
    filePath = input("Please enter the exact path of your latest Lynis security vulnerability report. It should be located at /var/log/lynis-report.dat.....")
    tempReport = parseFile(filePath)
    patchSuggestions(tempReport)


if __name__ == "__main__":
    main()



