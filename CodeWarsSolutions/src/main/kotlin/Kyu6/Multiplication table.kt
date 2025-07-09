package Kyu6

object KataSolution {
    fun multiplicationTable(size: Int): Array<IntArray> {
        var a= Array(size) { IntArray(size) }
        for(i in 0..size-1){
            for(j in 0..size-1) {
                a[i][j] = (i+1) * (j+1)
            }
        }
        return a
    }
}

fun main() {
    val size = 5 // Change this to the desired size of the multiplication table
    val table = KataSolution.multiplicationTable(size)

    // Print the elements of the multiplication table
    for (i in 0 until size) {
        for (j in 0 until size) {
            print("${table[i][j]}\t") // Use '\t' for tab spacing
        }
        println() // Move to the next row
    }
}