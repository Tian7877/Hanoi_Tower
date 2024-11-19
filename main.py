import tkinter as tk
import time
#Ngide tugas yang menarik lagi pak seru jga 
class Peg:

    def __init__(self, pegId, pegStatus):
        self.pegId = pegId
        self.pegStatus = pegStatus
        
    def IsEmpty(self):
        return True if self.pegStatus == [] else False

class HanoiTowerSolution:
    def __init__(self, numOfPegs, numOfDisks):
        assert numOfPegs >= 3 , "TIANG HARUS LEBIH DARI 3 WOY"
        self.numOfPegs = numOfPegs
        self.numOfDisks = numOfDisks
        
        # Inisiasi Best Solusi 
        self.dpBestSolution = [[[0, 0] for i in range(numOfDisks)] for i in range(numOfPegs - 2)]
        for i in range(1, self.numOfDisks + 1):
            self.dpBestSolution[0][i - 1] = [i, 2 ** i - 1]
        for i in range(1, self.numOfPegs - 2):
            self.dpBestSolution[i][0] = [1, 1]
            self.dpBestSolution[i][1] = [1, 3]          
        self.FindBestSolution(self.numOfDisks, self.numOfPegs)

        self.errorCount = 0
        self.stepCount = 0

        # Inisialisasi Tiang 
        self.pegArray = [Peg(0,[])]
        self.pegArray[0].pegStatus = [i for i in range(self.numOfDisks, 0, -1)]
        for i in range(1, self.numOfPegs):
            self.pegArray.append(Peg(i,[]))
        self.GeneralSolution(self.numOfDisks, self.numOfPegs, 0, 1, self.numOfPegs - 1)
        print("Least Move: ", self.dpBestSolution[-1][-1][1])
        print("Used Move: ", self.stepCount)
        print(self.errorCount, " Error Found")
        
    def GeneralSolution(self, N, P, sourceID, bufferID, destID):
        K = self.dpBestSolution[P - 3][N - 1][0]
        # Pake Hanoi Biasa aja cik 
        if N <= 2 or P <= 3 or K < 1:
            self.ClassicSolution(N, self.pegArray[sourceID], self.pegArray[bufferID], self.pegArray[destID])
        else:
            # Pindahin K nya dari sumber tiang ke tiang bantuan 
            self.GeneralSolution(K, P, sourceID, destID, bufferID)
            # Uodate Bantuan baru untuk move baru 
            newBuff = bufferID
            if self.EmptyPegs(destID) != []:
                newBuff = self.EmptyPegs(destID)[0]
            # Pindahkan disk kiri ke destinasi gunakkan bantuan tiang 
            self.GeneralSolution(N - K, P - 1, sourceID, newBuff, destID)
            # Pindahkan Disk Terakhir ke destinasi 
            self.GeneralSolution(K, P, bufferID, sourceID, destID)
            
    def ClassicSolution(self, N, srcPeg, bufPeg, dstPeg):
        if N == 1:
            # Check error apakah disk yang lebih kecil selalu diatas disk lebih besar 
            if dstPeg.pegStatus != [] and srcPeg.pegStatus[-1] > dstPeg.pegStatus[-1]:
                self.errorCount += 1
            # Pindahkan dari tianng asal ke tiang tujuan 
            dstPeg.pegStatus.append(srcPeg.pegStatus.pop())
            self.stepCount += 1
            self.PrintPegStatus()
        else:
            self.ClassicSolution(N - 1, srcPeg, dstPeg, bufPeg)
            self.ClassicSolution(1, srcPeg, bufPeg, dstPeg)
            self.ClassicSolution(N - 1, bufPeg, srcPeg, dstPeg)

    def FindBestSolution(self, N, P):
        #  (Boundary) (Basis Case)
        if N < 0 or P < 3:
            return -1
        # Hindari Repeat case 
        if self.dpBestSolution[P - 3][N - 1][1] != 0:
            return self.dpBestSolution[P - 3][N - 1][1]
        # Initialisi worst case
        leastMove = 2 * self.FindBestSolution(N - 1, P) + self.FindBestSolution(1, P - 1)
        K = N - 1
        # Traverse all cases
        for k in range(N - 2, 0, -1):        
                temp = 2 * self.FindBestSolution(k, P) + self.FindBestSolution(N - k, P - 1)
                if temp < leastMove:
                    leastMove = temp
                    K = k
                else:
                    break
        # Update DP Table
        self.dpBestSolution[P - 3][N - 1] = [K, leastMove]
        return leastMove
    
    def EmptyPegs(self, dstId):
        availablePegId = []
        for i in range(self.numOfPegs):
            if self.pegArray[i].IsEmpty() and (i != dstId):
                availablePegId.append(i)
        return availablePegId

    def PrintPegStatus(self):
        print("Step " + str(self.stepCount))
        for i in range(self.numOfPegs):
            print("Peg ", (i + 1), self.pegArray[i].pegStatus)
        print("----------------------------------------------------------------------")

#Desain Classic aja 
def on_enter_hover(event):
    event.widget.config(bg="blue")  # Warna ketika di-hover (biru tua)

def on_leave_hover(event):
     event.widget.config(bg="lightblue")  # Warna default (biru muda) 

class HanoiTowerSolutionWithVisual(HanoiTowerSolution):
    def __init__(self, numOfPegs, numOfDisks):
        self.numOfPegs = numOfPegs
        self.numOfDisks = numOfDisks
        self.visual_steps = []
        self.is_solution_computed = False
        self.init_visualization()
        super().__init__(numOfPegs, numOfDisks)

    def move_disk_visual(self, src, dest):
        self.visual_steps.append((src, dest))

    def ClassicSolution(self, N, srcPeg, bufPeg, dstPeg):
        if N == 1:
            if dstPeg.pegStatus and srcPeg.pegStatus[-1] > dstPeg.pegStatus[-1]:
                self.errorCount += 1
            dstPeg.pegStatus.append(srcPeg.pegStatus.pop())
            self.stepCount += 1
            self.move_disk_visual(srcPeg.pegId, dstPeg.pegId)
        else:
            self.ClassicSolution(N - 1, srcPeg, dstPeg, bufPeg)
            self.ClassicSolution(1, srcPeg, bufPeg, dstPeg)
            self.ClassicSolution(N - 1, bufPeg, srcPeg, dstPeg)

    def init_visualization(self):
        self.root = tk.Tk()
        self.root.title("Tower of Hanoi Visualization")

        self.root.geometry("1000x600")
        self.canvas = tk.Canvas(self.root, width=1000, height=500, bg="white")
        self.canvas.pack()
         
        self.title_label = tk.Label(self.root, text="Tower of Hanoi Visualization", font=("Arial", 20),bg="white")
        self.title_label.place(relx=0.5, rely=0.05, anchor="n")

        self.title_label = tk.Label(self.root, text="by:Christian VL Sebayang", font=("Arial", 14),bg="white")
        self.title_label.place(relx=0.5, rely=0.1, anchor="n")

        self.step_label = tk.Label(self.root, text="Moves : 0")
        self.step_label.pack()

        button_frame = tk.Frame(self.root)
        button_frame.pack()
        
        self.start_button = tk.Button(button_frame, text="Start", command=self.start_solution, bg="lightblue", fg="black")
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.start_button.bind("<Enter>", on_enter_hover)
        self.start_button.bind("<Leave>", on_leave_hover)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_visualization, bg="lightblue", fg="black")
        self.reset_button.pack(side=tk.LEFT, padx=10)
        self.reset_button.bind("<Enter>", on_enter_hover)
        self.reset_button.bind("<Leave>", on_leave_hover)

        self.peg_positions = [100 + i * 800 // (self.numOfPegs - 1) for i in range(self.numOfPegs)]
        self.disk_widths = [30 + i * 10 for i in range(self.numOfDisks)]
        self.disk_height = 20
        self.pegs = [[] for _ in range(self.numOfPegs)]
        self.disk_objects = {}

        

        for x in self.peg_positions:
            self.canvas.create_line(x, 450, x, 200, width=5)

        for i in range(self.numOfDisks, 0, -1):
            disk_id = self.canvas.create_rectangle(
                self.peg_positions[0] - self.disk_widths[i - 1] // 2,
                450 - (self.numOfDisks - i + 1) * self.disk_height,
                self.peg_positions[0] + self.disk_widths[i - 1] // 2,
                450 - (self.numOfDisks - i) * self.disk_height,
                fill="blue"
            )
            self.pegs[0].append(i)
            self.disk_objects[i] = disk_id

    def draw_pegs_and_disks(self):
        self.canvas.delete("all")
        for x in self.peg_positions:
            self.canvas.create_line(x, 450, x, 200, width=5)

        for i in range(self.numOfDisks, 0, -1):
            disk_id = self.canvas.create_rectangle(
                self.peg_positions[0] - self.disk_widths[i - 1] // 2,
                450 - (self.numOfDisks - i + 1) * self.disk_height,
                self.peg_positions[0] + self.disk_widths[i - 1] // 2,
                450 - (self.numOfDisks - i) * self.disk_height,
                fill="blue"
            )
            self.pegs[0].append(i)
            self.disk_objects[i] = disk_id

        for peg in self.pegs[1:]:
            peg.clear()

        self.step_label.config(text="Moves : 0")
        self.visual_steps = []
        self.is_solution_computed = False

    def reset_visualization(self):
        """Reset the visualization to the initial state."""
        self.pegs = [[] for _ in range(self.numOfPegs)]
        self.disk_objects = {}
        self.draw_pegs_and_disks()

    def start_solution(self):
        """Compute the solution and start the animation."""
        if not self.is_solution_computed:
            self.visual_steps = []
            super().__init__(self.numOfPegs, self.numOfDisks)
            self.is_solution_computed = True
        self.animate_solution()

    def animate_solution(self):
        for step, (src, dest) in enumerate(self.visual_steps):
            disk = self.pegs[src].pop()
            self.pegs[dest].append(disk)

            x1, x2 = (
                self.peg_positions[dest] - self.disk_widths[disk - 1] // 2,
                self.peg_positions[dest] + self.disk_widths[disk - 1] // 2,
            )
            y1 = 450 - len(self.pegs[dest]) * self.disk_height
            y2 = y1 + self.disk_height

            self.canvas.coords(
                self.disk_objects[disk],
                x1, y1, x2, y2,
            )
            self.step_label.config(text=f"Moves : {step + 1}")
            self.root.update()
            time.sleep(0.5)


# User input
numOfDisks = int(input("Enter number of disks : "))
numOfPegs = int(input("Enter number of pegs : "))
hanoi_visual = HanoiTowerSolutionWithVisual(numOfPegs, numOfDisks)
hanoi_visual.root.mainloop()
