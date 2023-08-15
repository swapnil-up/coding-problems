fun points(games: List<String>): Int {
    var score1:Int=0
    var score2=0
    var score=0
    games.forEach{gameResult->
        var key=gameResult.split(":")
        score1=(key[0].toInt())
        score2=(key[1].toInt())
        if (score1>score2) score+=3
        else if (score1==score2) score+=1
        else score
    }
    return(score)
}

fun main(){
        var e=points(listOf("1:0", "2:0", "3:0", "4:0", "2:1", "3:1", "4:1", "3:2", "4:2", "4:3"));
        var f=points(listOf("1:1", "2:2", "3:3", "4:4", "2:2", "3:3", "4:4", "3:3", "4:4", "4:4"));
//        printAndAssert(0, listOf("0:1", "0:2", "0:3", "0:4", "1:2", "1:3", "1:4", "2:3", "2:4", "3:4"));
//        printAndAssert(15, listOf("1:0", "2:0", "3:0", "4:0", "2:1", "1:3", "1:4", "2:3", "2:4", "3:4"));
//        printAndAssert(12, listOf("1:0", "2:0", "3:0", "4:4", "2:2", "3:3", "1:4", "2:3", "2:4", "3:4"));
    println("$e\n$f")
    }

