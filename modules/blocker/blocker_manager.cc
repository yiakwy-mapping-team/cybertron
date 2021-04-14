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

#include "modules/blocker/blocker_manager.h"

namespace apollo {
namespace cyber {
namespace blocker {

BlockerManager::BlockerManager() {}

BlockerManager::~BlockerManager() { blockers_.clear(); }

void BlockerManager::Observe() {
  std::lock_guard<std::mutex> lock(blocker_mutex_);
  for (auto& item : blockers_) {
    item.second->Observe();
  }
}

void BlockerManager::Reset() {
  std::lock_guard<std::mutex> lock(blocker_mutex_);
  for (auto& item : blockers_) {
    item.second->Reset();
  }
  blockers_.clear();
}

}  // namespace blocker
}  // namespace cyber
}  // namespace apollo
