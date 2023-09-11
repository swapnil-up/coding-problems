package Kyu8

class SmallestIntegerFinder {

    fun findSmallestInt(nums: List<Int>): Int {
        return nums.sorted().first()
    }

}

fun main() {
    val sif = SmallestIntegerFinder()
    println(sif.findSmallestInt(listOf(15, 20, 10, -17, 22, 9001)))
}