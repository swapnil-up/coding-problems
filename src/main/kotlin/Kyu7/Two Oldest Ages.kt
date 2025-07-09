package Kyu7

fun twoOldestAges(ages: List<Int>): List<Int> {
    return listOf(ages.sortedDescending()[1],ages.sortedDescending()[0])
}

fun main(){
    println(twoOldestAges(listOf(1,5,87,45,8,8)))
    println(twoOldestAges(listOf(6,5,83,5,3,18)))
}