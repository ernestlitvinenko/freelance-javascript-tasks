// Number 1
const data = [
    {'name': 'tower', 'speed': 0, 'hp': 100}, 
    {'name': 'ork', 'speed': 10, 'hp': 0}, 
    {'name': 'soldier', 'speed': 10, 'hp': 10}, 
    {'name': 'troll', 'speed': 10, 'hp': -1}, 
    {'name': 'ruin', 'speed': 0, 'hp': -100}, 
    {'name': 'rock', 'speed': 0, 'hp': 0}, 
    {'name': 'castle', 'speed': 0, 'hp': 999}, 
    {'name': 'bird', 'speed': 100, 'hp': 0.1}, 
]

const outputList = []

data.forEach(elem => {if (elem.hp > 0 && elem.speed === 0) outputList.push(elem)})

console.log(outputList)


// Number 2
MAX_NUMBER = Math.pow(2, 32) - 1

function findSlowestUnit(units) {
    // Don't use var instead let and const
    let slowestUnit = null
    let minSpeed = MAX_NUMBER
    
    units.forEach(currentUnit => {if (currentUnit.speed < minSpeed) {slowestUnit = currentUnit; minSpeed = currentUnit.speed}})
    return slowestUnit
}

console.log(findSlowestUnit(data))
