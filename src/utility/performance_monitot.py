class PerformanceMonitor:
    def track_metrics(self):
        return {"CPU": 10, "GPU": 15, "NPU": 5}  # Example metrics
    
    def display_metrics(self):
        metrics = self.track_metrics()
        print(f"Performance Metrics: {metrics}")
