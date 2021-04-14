/******************************************************************************
 * Copyright 2018 The Apollo Authors. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *****************************************************************************/

#ifndef CYBER_SCHEDULER_SCHEDULER_FACTORY_H_
#define CYBER_SCHEDULER_SCHEDULER_FACTORY_H_

#include "modules/common/environment.h"
#include "modules/common/file.h"
#include "modules/common/global_data.h"
#include "modules/common/util.h"
#include "modules/scheduler/policy/scheduler_choreography.h"
#include "modules/scheduler/policy/scheduler_classic.h"
#include "modules/scheduler/scheduler.h"

namespace apollo {
namespace cyber {
namespace scheduler {

Scheduler* Instance();
void CleanUp();

}  // namespace scheduler
}  // namespace cyber
}  // namespace apollo

#endif  // CYBER_SCHEDULER_SCHEDULER_FACTORY_H_
