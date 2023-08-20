package Kyu7

class LatinSquares {
    companion object {
        fun makeLatinSquare(n: Int): Array<IntArray> {
            val latinSquare = Array(n) { IntArray(n) }
            for(i in 0..n-1) {
                for(j in 0..n-1){
                    latinSquare[i][(j+i)%n]=j+1
                }
            }
            return latinSquare
        }
    }
}

fun main(){
    for (i in 1..10) {
        var latinSquare=LatinSquares.makeLatinSquare(i)
        for(j in 0..i-1){
            for(k in 0..i-1){
                print(latinSquare[j][k])
            }
            println()
        }
        println()
    }

}
