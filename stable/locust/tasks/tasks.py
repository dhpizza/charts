from locust import HttpLocust, TaskSet, task

class ElbTasks(TaskSet):
  @task
  def getHome(self):
      self.client.get("/")
  @task
  def getOwners(self):
      self.client.get("/owners/")
  @task
  def getVets(self):
      self.client.get("/vets/")
  @task
  def findOwners(self):
      self.client.get("/owners/find/")

class ElbWarmer(HttpLocust):
  task_set = ElbTasks
  min_wait = 1000
  max_wait = 3000
