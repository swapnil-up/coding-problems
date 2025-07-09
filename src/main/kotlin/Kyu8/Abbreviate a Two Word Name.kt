package Kyu8

fun abbrevName(name:String) = name.substring(0,1).uppercase()+"."+name.substring(name.indexOf(" ")+1,name.indexOf(" ")+2).uppercase()

fun main() {
    println(abbrevName("Sam Harris"))
    println(abbrevName("Patrick Feenan"))
    println(abbrevName("Evan Cole"))
    println(abbrevName("P Favuzzi"))
    println(abbrevName("David Mendieta"))
}