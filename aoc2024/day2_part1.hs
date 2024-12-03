
import Data.List (sort)
import System.IO (hIsEOF, stdin)

checkSafety :: [Int] -> Int -> Int -> Bool 
checkSafety lst n i
    | i == n - 1 = True 
    | abs((lst !! i) - (lst !! (i + 1))) < 1 || abs((lst !! i) - (lst !! (i + 1))) > 3 = False
    | otherwise = checkSafety lst n (i + 1)

checkIncreasing :: [Int] -> Int -> Int -> Bool
checkIncreasing lst n i
    | i == n - 1 = True
    | (lst !! i) > (lst !! (i + 1)) = False
    | otherwise = checkIncreasing lst n (i + 1)

checkDecreasing :: [Int] -> Int -> Int -> Bool
checkDecreasing lst n i
    | i == n - 1 = True
    | (lst !! i) < (lst !! (i + 1)) = False
    | otherwise = checkDecreasing lst n (i + 1)

processLists :: IO (Int)
processLists = do
    eof <- hIsEOF stdin
    if eof
        then return 0
        else do
            input <- getLine
            let lst = map read (words input) :: [Int] 
            let n = length lst 
            let isDecreasing = checkDecreasing lst n 0
            let isIncreasing = checkIncreasing lst n 0
            let isSafe = checkSafety lst n 0
            result <- processLists 
            if (isDecreasing || isIncreasing) && isSafe
                then return (1 + result)
                else do
                    return result

            

main :: IO ()
main = do
    cnt <- processLists
    print cnt 

