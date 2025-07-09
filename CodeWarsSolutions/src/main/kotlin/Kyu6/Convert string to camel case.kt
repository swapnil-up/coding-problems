package Kyu6

fun toCamelCase(str:String):String = str.split("-","_")[0]+str.split("-","_").drop(1).joinToString("" ){it.capitalize()}

// it.subSequence(1,str.split("_","-".length))
fun main() {
    println(toCamelCase(""))
    println(toCamelCase("the_stealth_warrior"))
    println(toCamelCase("The-Stealth-Warrior"))
    println(toCamelCase("A-B-C"))
}