; Enter your code here. Read input from STDIN. Print output to STDOUT
;
(let [sc (java.util.Scanner. *in*)
      testcases (.nextInt sc)
      bst-count ((memoize (fn [n]
             (loop [n_ 1 c [1 1]]
               (if (= n_ n)
                 c
                 (recur 
                  
                   (inc n_) 
                   (conj c 
                         (reduce 
                           #(mod (+ %1 %2) 100000007)  (for [i (range 0 (inc n_))]
                               (mod (* (nth c i) (nth c (- n_ i))) 100000007))))))))) 1000)
      ]
  (doseq [i (range 0 testcases)]
      (println (nth bst-count (.nextInt sc)))))