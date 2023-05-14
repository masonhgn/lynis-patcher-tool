# lynis-patcher-tool
Python tool for patching vulnerabilities found by the Lynis tool.


## GOAL: To create a portable, robust tool that will take a Lynis generated security audit report and fix all of the vulnerabilities found.

# CURRENT PROBLEMS:
- Security auditing is very specific to the purpose of the machine, and usually there will be some settings and conditions of a machine that are necessary to have regardless of the fact that Lynis may flag it as a vulnerability. It is not a good idea to blindly patch all vulnerabilities that are found by Lynis without proper understanding of the impact and possible consequences. Some vulnerabilities might be false positives.


With this in mind, my current approach is as follows:


commands.py has a python dictionary that contains suggestions, mapping to the commands that will deal with those suggestions.

1. Parse Lynis report: This entails generating a Lynis report, and providing the exact file path. This will be given as input into the program as there may be multiple reports that have been generated.

2. Pass all suggestions through the suggestions dictionary for further redirection: This will take all suggestions Lynis generates and find its corresponding command in the aforementioned commands python dictionary.

3. Run the commands that map to the provided suggestions, thereby following all suggestions.

![image](https://user-images.githubusercontent.com/73012906/236694965-c485d0c4-126e-4f09-a2a2-adc84b276b18.png)

