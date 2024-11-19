import tkinter as tk
import time


class Peg:
    def __init__(self, pegId, pegStatus):
        self.pegId = pegId
        self.pegStatus = pegStatus

    def IsEmpty(self):
        return True if self.pegStatus == [] else False


class HanoiTowerSolution:
    def __init__(self, numOfPegs, numOfDisks):
        assert numOfPegs >= 3, "TIANG HARUS LEBIH DARI 3 WOY"
        self.numOfPegs = numOfPegs
        self.numOfDisks = numOfDisks

        # Inisiasi Best Solusi
        self.dpBestSolution = [[[0, 0] for i in range(numOfDisks)] for i in range(numOfPegs - 2)]
        for i in range(1, self.numOfDisks + 1):
            self.dpBestSolution[0][i - 1] = [i, 2**i - 1]
        for i in range(1, self.numOfPegs - 2):
            self.dpBestSolution[i][0] = [1, 1]
            self.dpBestSolution[i][1] = [1, 3]
        self.FindBestSolution(self.numOfDisks, self.numOfPegs)

        self.errorCount = 0
        self.stepCount = 0

        # Inisialisasi Tiang
        self.pegArray = [Peg(0, [])]
        self.pegArray[0].pegStatus = [i for i in range(self.numOfDisks, 0, -1)]
        for i in range(1, self.numOfPegs):
            self.pegArray.append(Peg(i, []))

        self.visual_steps = []
        self.GeneralSolution(self.numOfDisks, self.numOfPegs, 0, 1, self.numOfPegs - 1)

    def GeneralSolution(self, N, P, sourceID, bufferID, destID):
        K = self.dpBestSolution[P - 3][N - 1][0]
        if N <= 2 or P <= 3 or K < 1:
            self.ClassicSolution(N, self.pegArray[sourceID], self.pegArray[bufferID], self.pegArray[destID])
        else:
            self.GeneralSolution(K, P, sourceID, destID, bufferID)
            newBuff = bufferID
            if self.EmptyPegs(destID) != []:
                newBuff = self.EmptyPegs(destID)[0]
            self.GeneralSolution(N - K, P - 1, sourceID, newBuff, destID)
            self.GeneralSolution(K, P, bufferID, sourceID, destID)

    def ClassicSolution(self, N, srcPeg, bufPeg, dstPeg):
        if N == 1:
            if dstPeg.pegStatus != [] and srcPeg.pegStatus[-1] > dstPeg.pegStatus[-1]:
                self.errorCount += 1
            dstPeg.pegStatus.append(srcPeg.pegStatus.pop())
            self.stepCount += 1
            self.visual_steps.append((srcPeg.pegId, dstPeg.pegId))
        else:
            self.ClassicSolution(N - 1, srcPeg, dstPeg, bufPeg)
            self.ClassicSolution(1, srcPeg, bufPeg, dstPeg)
            self.ClassicSolution(N - 1, bufPeg, srcPeg, dstPeg)

    def FindBestSolution(self, N, P):
        if N < 0 or P < 3:
            return -1
        if self.dpBestSolution[P - 3][N - 1][1] != 0:
            return self.dpBestSolution[P - 3][N - 1][1]
        leastMove = 2 * self.FindBestSolution(N - 1, P) + self.FindBestSolution(1, P - 1)
        K = N - 1
        for k in range(N - 2, 0, -1):
            temp = 2 * self.FindBestSolution(k, P) + self.FindBestSolution(N - k, P - 1)
            if temp < leastMove:
                leastMove = temp
                K = k
            else:
                break
        self.dpBestSolution[P - 3][N - 1] = [K, leastMove]
        return leastMove

    def EmptyPegs(self, dstId):
        availablePegId = []
        for i in range(self.numOfPegs):
            if self.pegArray[i].IsEmpty() and (i != dstId):
                availablePegId.append(i)
        return availablePegId


class HanoiVisualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tower of Hanoi Visualization")
        self.root.geometry("1000x600")
        self.init_ui()

    def init_ui(self):
        title_label = tk.Label(self.root, text="Tower of Hanoi", font=("Arial", 20))
        title_label.pack()

        input_frame = tk.Frame(self.root)
        input_frame.pack()

        tk.Label(input_frame, text="Number of Pegs: ").grid(row=0, column=0, padx=5)
        self.pegs_entry = tk.Entry(input_frame)
        self.pegs_entry.grid(row=0, column=1, padx=5)
        self.pegs_entry.insert(0, "3")

        tk.Label(input_frame, text="Number of Disks: ").grid(row=1, column=0, padx=5)
        self.disks_entry = tk.Entry(input_frame)
        self.disks_entry.grid(row=1, column=1, padx=5)
        self.disks_entry.insert(0, "3")

        self.move_label = tk.Label(self.root, text="Moves: 0", font=("Arial", 12))
        self.move_label.pack(pady=10)

        start_button = tk.Button(self.root, text="Start", command=self.start_solution)
        start_button.pack(pady=10)

        self.canvas = tk.Canvas(self.root, width=1000, height=400, bg="white")
        self.canvas.pack()

    def start_solution(self):
        num_pegs = int(self.pegs_entry.get())
        num_disks = int(self.disks_entry.get())

        hanoi = HanoiTowerSolution(num_pegs, num_disks)
        self.visualize(hanoi.visual_steps, hanoi.numOfDisks, hanoi.numOfPegs)

    def visualize(self, steps, num_disks, num_pegs):
        self.canvas.delete("all")
        peg_positions = [100 + i * 800 // (num_pegs - 1) for i in range(num_pegs)]
        disk_widths = [30 + i * 10 for i in range(num_disks)]
        disk_height = 20

        pegs = [[] for _ in range(num_pegs)]
        disks = {}

        # Draw pegs
        for i, x in enumerate(peg_positions):
            self.canvas.create_line(x, 100, x, 400, width=5, fill="black")

        for i in range(num_disks, 0, -1):
            x1 = peg_positions[0] - disk_widths[i - 1] // 2
            x2 = peg_positions[0] + disk_widths[i - 1] // 2
            y1 = 400 - len(pegs[0]) * disk_height
            y2 = y1 - disk_height
            disk = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            disks[i] = disk
            pegs[0].append(i)

        # Animate moves
        for i, (src, dst) in enumerate(steps):
            time.sleep(0.5)
            self.move_label.config(text=f"Moves: {i + 1}")
            self.root.update()

            disk = pegs[src].pop()
            pegs[dst].append(disk)

            x1 = peg_positions[dst] - disk_widths[disk - 1] // 2
            x2 = peg_positions[dst] + disk_widths[disk - 1] // 2
            y1 = 400 - len(pegs[dst]) * disk_height
            y2 = y1 - disk_height

            self.canvas.coords(disks[disk], x1, y1, x2, y2)

        self.move_label.config(text=f"Moves: {len(steps)} (Complete)")


HanoiVisualizer().root.mainloop()
