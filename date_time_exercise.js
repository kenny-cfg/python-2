const now = new Date()

console.log(now)

const formatted = now.toDateString('%a %d %b %H:%M:%S') + ' '
 + now.toTimeString('%H:%M:%S')

console.log(formatted)