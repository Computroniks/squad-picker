const prompt = require('prompt-sync')({sigint: true});
var swimmerList = {}
var squad1 = []
var squad2 = []
var squad3 = []
var noSquad = []
var version = '1.0.0'
var choice
var state
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
function addSwimmer(){
    var minSessions = null
    var averageTime = null
    var swimmerName = prompt('Please enter the name of your swimmer:\n')
    if (!(swimmerName in swimmerList)){
        var choice = prompt('A swimmer with this name already exists. Do you want to overwrite them? [y/n]').toLowerCase()
        while (true){
            if(choice !='y' && choice !='n'){
                choice = prompt('Do you want to overwrite them? [y/n]').toLowerCase()
            }
            else{
                break
            }
        }
        if (choice == 'n'){
            return false
        }
    }
    while (true){
        try{
            minSessions = parseInt(prompt('Please enter the minimum number of sessions the swimmer is willing to do:\n'),10)
            break
        }
        catch(err){
            console.log('A valid number is required')
        }
    }
    while(true){
        try{
            averageTime = parseFloat(prompt('Please enter the average time it takes the swimmer to swim 50m in seconds:\n'))
            break
        }
        catch(err){
            console.log('A valid number is required')
        }
    }
    swimmerList[swimmerName] = {'minSessions':minSessions, 'averageTime':averageTime}
    return true

}
console.log(`Squad chooser Version: ${version} \nCopyright (c) 2020 Matthew Nickson, All rights reserved\nLicensed under MIT`)
while (true){
    //TODO: This causes infinte loop. Needs to pause for input
    console.log('[1] Add swimmer\n[2] Generate squads\n[3] Quit')
    readline.question('Please choose an option: ', (answer) => {
        choice = parseInt(answer, 10)
        if (choice == 1){
            state = addSwimmer()
            if (state){
                console.log('Successfully added swimmer')
            }
            else{
                console.log('Failed to add swimmer')
            }
        }
    })
    
}