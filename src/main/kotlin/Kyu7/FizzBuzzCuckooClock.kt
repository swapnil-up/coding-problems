package Kyu7

fun fizzBuzzCuckooClock(time: String) : String {
    var timing=time.split(":")
    var hour=timing[0].toInt()%12
    var min=timing[1].toInt()
    if (min%3==0 && min%5==0){
        if (min==0) {
            if (hour==0) return "Cuckoo ".repeat(12).trim()
            else return "Cuckoo ".repeat(hour).trim()
        }
        else if (min==30) return "Cuckoo"
        else return "Fizz Buzz"
    }
    else{
        if (min%3==0) return "Fizz"
        else if (min%5==0) return "Buzz"
        else return "tick"
    }
}

fun main () {
    println("Testing with time 13:34")
    println((fizzBuzzCuckooClock("13:34")))
    println("Testing with time 21:00")
    println((fizzBuzzCuckooClock("21:00")))
    println("Testing with time 11:15")
    println((fizzBuzzCuckooClock("11:15")))
    println("Testing with time 03:03")
    println((fizzBuzzCuckooClock("03:03")))
    println("Testing with time 14:30")
    println((fizzBuzzCuckooClock("14:30")))
    println("Testing with time 08:55")
    println((fizzBuzzCuckooClock("08:55")))
    println("Testing with time 00:00")
    println((fizzBuzzCuckooClock("00:00")))
    println("Testing with time 12:00")
    println((fizzBuzzCuckooClock("12:00")))
}