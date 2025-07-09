package Kyu8

fun feast(beast: String, dish: String): Boolean {
    if (beast.first()==dish.first() && beast.last()==dish.last()) return true
    else return false
}

fun main(){
    println(feast("great blue heron", "garlic naan"))
    println(feast("chickadee", "chocolate cake"))
    println(feast("brown bear", "bear claw"))
    println(feast("marmot", "mulberry tart"))
    println(feast("porcupine", "pie"))
    println(feast("electric eel", "lasagna"))
    println(feast("slow loris", "salsas"))
    println(feast("ox", "orange lox"))
    println(feast("blue-footed booby", "blueberry"))
}