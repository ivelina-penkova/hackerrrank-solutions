; Enter your code here. Read input from STDIN. Print output to STDOUT
;

(require 'clojure.string)

(defn build-tree-map
  []
  (let [n (Integer/parseInt (read-line))]
    (loop [i 1 tree {}]
      (if (> i n) tree
          (let [[a b] (clojure.string/split (read-line) #"\s+")]
            (recur (inc i)
                   (conj tree
                         [i [(Integer/parseInt a) (Integer/parseInt b)]])))))))

(defn build-tree
  [tree-map root-idx]
  (if (= root-idx -1)
    []
    (let [[left-idx right-idx] (tree-map root-idx)]
      [root-idx
       (build-tree tree-map left-idx)
       (build-tree tree-map right-idx)])))

(defn fold-tree-inorder
  [f init node]
  (if (empty? node)
    init
    (let [[root-idx left right] node]
      (f (fold-tree-inorder f init left)
         root-idx
         (fold-tree-inorder f init right)))))

;; (defn print-tree-inorder
;;   [tree]
;;   (println (clojure.string/join
;;             " "
;;             (fold-tree-inorder #(concat %1 [%2] %3) [] tree))))
(defn print-tree-inorder-helper
  [node]
  (let [[root-idx left right] node]
    (do
      (when (not (empty? left))
        (print-tree-inorder-helper left)
        (print " "))
      (print root-idx)
      (when (not (empty? right))
        (print " ")
        (print-tree-inorder-helper right)))))
(defn print-tree-inorder
  [node]
  (do
    (print-tree-inorder-helper node)
    (println)))

(defn swap-nodes
  [k depth node]
  (if (empty? node)
    []
    (let [[root-idx left right] node]
      (if (= 0 (mod depth k))
        [root-idx
         (swap-nodes k (inc depth) right)
         (swap-nodes k (inc depth) left)]
        [root-idx
         (swap-nodes k (inc depth) left)
         (swap-nodes k (inc depth) right)]))))


(let [tree (build-tree (build-tree-map) 1)
      n-tests (Integer/parseInt (read-line))]
  (do
    ;;(println tree)
    (loop [t n-tests tree tree]
      (when (> t 0)
        (let [k (Integer/parseInt (read-line))
              swapped-tree (swap-nodes k 1 tree)]
          (do
            (print-tree-inorder swapped-tree)
            (recur (dec t) swapped-tree)))))))