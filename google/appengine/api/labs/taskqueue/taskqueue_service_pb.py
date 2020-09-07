#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#




"""A shim to access the new taskqueue_service_pb module.

This contains all of the protocol messages as of 1.4.2.
"""




from google.appengine.api.taskqueue import taskqueue_service_pb


TaskQueueServiceError = taskqueue_service_pb.TaskQueueServiceError
TaskQueueRetryParameters = taskqueue_service_pb.TaskQueueRetryParameters
TaskQueueAddRequest_Header = taskqueue_service_pb.TaskQueueAddRequest_Header
TaskQueueAddRequest_CronTimetable = taskqueue_service_pb.TaskQueueAddRequest_CronTimetable
TaskQueueAddRequest = taskqueue_service_pb.TaskQueueAddRequest
TaskQueueAddResponse = taskqueue_service_pb.TaskQueueAddResponse
TaskQueueBulkAddRequest = taskqueue_service_pb.TaskQueueBulkAddRequest
TaskQueueBulkAddResponse_TaskResult = taskqueue_service_pb.TaskQueueBulkAddResponse_TaskResult
TaskQueueBulkAddResponse = taskqueue_service_pb.TaskQueueBulkAddResponse
TaskQueueDeleteRequest = taskqueue_service_pb.TaskQueueDeleteRequest
TaskQueueDeleteResponse = taskqueue_service_pb.TaskQueueDeleteResponse
TaskQueueForceRunRequest = taskqueue_service_pb.TaskQueueForceRunRequest
TaskQueueForceRunResponse = taskqueue_service_pb.TaskQueueForceRunResponse
TaskQueueUpdateQueueRequest = taskqueue_service_pb.TaskQueueUpdateQueueRequest
TaskQueueUpdateQueueResponse = taskqueue_service_pb.TaskQueueUpdateQueueResponse
TaskQueueFetchQueuesRequest = taskqueue_service_pb.TaskQueueFetchQueuesRequest
TaskQueueFetchQueuesResponse_Queue = taskqueue_service_pb.TaskQueueFetchQueuesResponse_Queue
TaskQueueFetchQueuesResponse = taskqueue_service_pb.TaskQueueFetchQueuesResponse
TaskQueueFetchQueueStatsRequest = taskqueue_service_pb.TaskQueueFetchQueueStatsRequest
TaskQueueScannerQueueInfo = taskqueue_service_pb.TaskQueueScannerQueueInfo
TaskQueueFetchQueueStatsResponse_QueueStats = taskqueue_service_pb.TaskQueueFetchQueueStatsResponse_QueueStats
TaskQueueFetchQueueStatsResponse = taskqueue_service_pb.TaskQueueFetchQueueStatsResponse
TaskQueuePauseQueueRequest = taskqueue_service_pb.TaskQueuePauseQueueRequest
TaskQueuePauseQueueResponse = taskqueue_service_pb.TaskQueuePauseQueueResponse
TaskQueuePurgeQueueRequest = taskqueue_service_pb.TaskQueuePurgeQueueRequest
TaskQueuePurgeQueueResponse = taskqueue_service_pb.TaskQueuePurgeQueueResponse
TaskQueueDeleteQueueRequest = taskqueue_service_pb.TaskQueueDeleteQueueRequest
TaskQueueDeleteQueueResponse = taskqueue_service_pb.TaskQueueDeleteQueueResponse
TaskQueueDeleteGroupRequest = taskqueue_service_pb.TaskQueueDeleteGroupRequest
TaskQueueDeleteGroupResponse = taskqueue_service_pb.TaskQueueDeleteGroupResponse
TaskQueueQueryTasksRequest = taskqueue_service_pb.TaskQueueQueryTasksRequest
TaskQueueQueryTasksResponse_TaskHeader = taskqueue_service_pb.TaskQueueQueryTasksResponse_TaskHeader
TaskQueueQueryTasksResponse_TaskCronTimetable = taskqueue_service_pb.TaskQueueQueryTasksResponse_TaskCronTimetable
TaskQueueQueryTasksResponse_TaskRunLog = taskqueue_service_pb.TaskQueueQueryTasksResponse_TaskRunLog
TaskQueueQueryTasksResponse_Task = taskqueue_service_pb.TaskQueueQueryTasksResponse_Task
TaskQueueQueryTasksResponse = taskqueue_service_pb.TaskQueueQueryTasksResponse
TaskQueueUpdateStorageLimitRequest = taskqueue_service_pb.TaskQueueUpdateStorageLimitRequest
TaskQueueUpdateStorageLimitResponse = taskqueue_service_pb.TaskQueueUpdateStorageLimitResponse
